async function sendJsonAndGetZip(jsonText) {
    /*
    Public: https://desirable-courage-production.up.railway.app/api/convert
    Private: http://127.0.0.1:5000/api/convert
    */

    const apiUrl = "http://127.0.0.1:5000/api/convert";
    const response = await fetch(apiUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: jsonText
    });

    if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
    }

    return await response.blob();
}

async function getQuestionTypes() {
    return await fetch('./data/question_types.json', {cache: "no-store"})
        .then((response) => {
            if (!response.ok) {
                throw new Error("Couldn't find JSON file.");
            }
            return response.json();
    })
}

async function getMathTypes() {
    return await fetch('./data/math_types.json', {cache: "no-store"})
        .then((response) => {
            if (!response.ok) {
                throw new Error("Couldn't find JSON file.");
            }
            return response.json();
    })
}

function downloadZip(blob, filename) {
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

function utf8_to_b64( str ) {
    return window.btoa(unescape(encodeURIComponent( str )));
}

// Submit the form

document.getElementById("json_submit").addEventListener("click", async (e) => {
    e.preventDefault();

    const downloadDiv = document.getElementById("download_div");
    downloadDiv.innerHTML = '';

    let final_json = {};

    const dateString = document.getElementById("json_date").value.replace(/-/g, '\/');
    const today =  dateString ? new Date(dateString) : new Date();

    const todayString = today.toLocaleDateString();

    final_json.project = document.getElementById("json_project").value || document.getElementById("json_project").placeholder;
    final_json.title = document.getElementById("json_title").value || document.getElementById("json_title").placeholder;
    final_json.double_column = document.getElementById("json_double_column").checked;
    final_json.date = todayString;
    final_json.author = document.getElementById("json_author").value || document.getElementById("json_author").placeholder;
    final_json.description = document.getElementById("json_description").value || document.getElementById("json_description").placeholder;
    final_json.question_keyword = document.getElementById("json_question_keyword").value || document.getElementById("json_question_keyword").placeholder;
    final_json.students = document.getElementById("json_students").value || document.getElementById("json_students").placeholder;
    final_json.students = final_json.students.replace(/\s/g, '').split(',');
    final_json.questions = getQuestions();
            
    final_json.description = utf8_to_b64(final_json.description);
    
    final_json = JSON.stringify(final_json);

    try {
        const zipBlob = await sendJsonAndGetZip(final_json);
        const downloadBtn = document.createElement("button");
        downloadBtn.textContent = "Descargar";
        downloadBtn.id = "downloadBtn";
        downloadDiv.appendChild(downloadBtn);

        downloadBtn.onclick = (e) => {
            e.preventDefault();
            if (zipBlob) {
                downloadZip(zipBlob, "project.zip");
            } else {
                throw new Error("Error al recibir el archivo");
            }
        }
    } catch(err) {
        window.alert("Algo salio mal...");
    }
})

const questionArray = document.getElementById("question_array");

function getQuestions() {
    let questions = [];

    for (const child of questionArray.childNodes) {

        if (child.nodeName.toLowerCase() != "div") {
            continue;
        }
        
        const selectElement = child.querySelector('select');
        const questionType = selectElement.value

        switch (questionType) {
            case "generic":
                {
                const firstContainer = child.querySelector('div');
                const statement = firstContainer.querySelector('input[placeholder="Enunciado"]').value
                const options = firstContainer.querySelector('input[placeholder="Elecciones"]').value
                const answer = firstContainer.querySelector('input[placeholder="Respuesta"]').value

                if (!(statement && options && answer)) {continue}

                let question = {};

                question.type = "generic";
                question.statement = utf8_to_b64(statement);
                question.choices = [utf8_to_b64(options)];
                question.answer = utf8_to_b64(answer);

                questions.push(question);
                }
                break;
            case "math":
                {
                const firstContainer = child.querySelector('div');
                const statement = firstContainer.querySelector('input[placeholder="Enunciado"]').value || " ";
                const questionQuantity = firstContainer.querySelector('input[placeholder="Cantidad de preguntas"]').value;



                const category = firstContainer.querySelector('select').value;

                if (!(statement && questionQuantity && category)) {continue}

                const secondContainer = firstContainer.querySelector('div');
                const subcategory = secondContainer.querySelector('select').value;

                if (!subcategory) {continue}

                const thirdContainer = secondContainer.querySelector('div');
                const operation = thirdContainer.querySelector('select').getAttribute("method");
                if (!operation) {continue}

                const fourthContainer = thirdContainer.querySelector('div');
                let configuration = {};

                for (const config of fourthContainer.childNodes) {
                    const input = config.querySelector('input')
                    const configName = config.textContent;
                    const configValue = input.value || input.placeholder;

                    configuration[configName] = Number.parseInt(configValue);
                }

                let question = {};

                question.type = "math";
                question.statement = utf8_to_b64(statement);
                question.quantity = Number.parseInt(questionQuantity);
                question.operation = operation;
                question.configuration = configuration;

                questions.push(question);
                }
                break;
            case "ai_prompt":
                {
                const firstContainer = child.querySelector('div');
                const prompt = firstContainer.querySelector('input[placeholder="Descripción de la pregunta"]').value
                const quantity = firstContainer.querySelector('input[placeholder="Cantidad de preguntas"]').value
                const answerCount = firstContainer.querySelector('input[placeholder="Cantidad de respuestas de opción múltiple"]').value

                if (!(prompt && quantity && answerCount)) {continue}

                let question = {};

                question.type = "ai_prompt";
                question.prompt = prompt;
                question.quantity = Number(quantity);
                question.answer_count = Number(answerCount);

                questions.push(question);
                }
            default:
                break;
        }
    }

    return questions;
}

function createStatement(parent, placeholder) {
    const statement = document.createElement("input");
    statement.type = "text";
    statement.placeholder = placeholder;
    parent.appendChild(statement);
    parent.appendChild(document.createElement("br"));
}

function createNumericStatement(parent, placeholder) {
    const statement = document.createElement("input");
    statement.type = "number";
    statement.placeholder = placeholder;
    parent.appendChild(statement);
    parent.appendChild(document.createElement("br"));
}

function createQuestion(questionTypesJson, mathTypesJson) {
    const question = document.createElement("div");
    const questionNumber = document.getElementById("question_array").childElementCount + 1;
    question.textContent = "Pregunta " + questionNumber;

    question.appendChild(document.createElement("br"))

    const category = document.createElement("select");
    const defaultOption = document.createElement("option");

    defaultOption.textContent = "Elija una categoría";
    defaultOption.disabled = true;
    defaultOption.selected = true;
    category.appendChild(defaultOption);

    questionTypesJson.forEach(element => {
        const option = document.createElement("option");
        option.value = element.method;
        option.textContent = element.label;
        category.appendChild(option);
    });

    const firstContainer = document.createElement("div");
    

    category.addEventListener("change", (e) => {
        const option = e.target.value;

        firstContainer.innerHTML = '';

        switch (option){
            case "generic":
                createStatement(firstContainer, "Enunciado");
                createStatement(firstContainer, "Elecciones");
                createStatement(firstContainer, "Respuesta");
                break;
            case "math":
                createStatement(firstContainer, "Enunciado");
                createNumericStatement(firstContainer, "Cantidad de preguntas");
                mathQuestion(firstContainer, mathTypesJson);
                break;
            case "ai_prompt":
                createStatement(firstContainer, "Descripción de la pregunta");
                createNumericStatement(firstContainer, "Cantidad de preguntas");
                createNumericStatement(firstContainer, "Cantidad de respuestas de opción múltiple");
                break;
            default:
                break;
        }
    })

    question.appendChild(category);
    question.appendChild(firstContainer);

    return question
}

document.getElementById("add_question").addEventListener("click", async (e) => {
    e.preventDefault();

    const questionTypesJson = await getQuestionTypes();
    const mathTypesJson = await getMathTypes();

    console.log(mathTypesJson);

    const question = createQuestion(questionTypesJson, mathTypesJson);
    questionArray.appendChild(question);
})
document.getElementById("del_question").addEventListener("click", (e) => {
    e.preventDefault();
    const children = questionArray.children
    if (children.length < 1) {
        console.warn("Not enough children");
        return;
    }
    questionArray.removeChild(questionArray.lastChild);
})

function mathQuestion(firstContainer, mathTypesJson) {
    const category = document.createElement("select");
    const defaultOption = document.createElement("option");

    defaultOption.textContent = "Elija una categoría";
    defaultOption.disabled = true;
    defaultOption.selected = true;
    category.appendChild(defaultOption);

    mathTypesJson.forEach((element, index) => {
        const option = document.createElement("option");
        option.value = index;
        option.textContent = element.label;
        category.appendChild(option);
    });

    const secondContainer = document.createElement("div")

    category.addEventListener("change", e => {
        const categoryIndex = e.target.value;

        secondContainer.innerHTML = '';

        const subcategory = document.createElement("select")
        const defaultOption = document.createElement("option");

        defaultOption.textContent = "Elija una subcategoría";
        defaultOption.disabled = true;
        defaultOption.selected = true;
        subcategory.appendChild(defaultOption)

        const subcategories = mathTypesJson[categoryIndex].subcategories;
        subcategories.forEach((element, index) => {
            const option = document.createElement("option");
            option.value = index;
            option.textContent = element.label;
            subcategory.appendChild(option);
        })

        const thirdContainer = document.createElement("div");

        subcategory.addEventListener("change", e => {
            const subcategoryIndex = e.target.value;

            thirdContainer.innerHTML = '';

            const operation = document.createElement("select");
            const defaultOption = document.createElement("option");

            defaultOption.textContent = "Elija una operación";
            defaultOption.disabled = true;
            defaultOption.selected = true;
            operation.appendChild(defaultOption)

            const operations = subcategories[subcategoryIndex].operations;

            operations.forEach((element, index) => {
                const option = document.createElement("option");
                option.value = index;
                option.textContent = element.label;

                option.setAttribute("method", element.method);

                operation.appendChild(option);
            })

            const fourthContainer = document.createElement("div");

            operation.addEventListener("change", e => {
                const operationIndex = e.target.value;

                const operationName = e.target.querySelector('option[value="' + operationIndex + '"]').getAttribute("method");
                operation.setAttribute("method", operationName);
                fourthContainer.innerHTML = '';

                const configuration = operations[operationIndex].configuration;
                const keys = Object.keys(configuration)
                for (let key of keys) {
                    const label = document.createElement("label");
                    label.textContent = key;
                    fourthContainer.appendChild(label);
                    createStatement(label, configuration[key]);
                }
            })

            thirdContainer.appendChild(operation);
            thirdContainer.appendChild(fourthContainer);
        });


        secondContainer.appendChild(subcategory);
        secondContainer.appendChild(thirdContainer);
    });

    firstContainer.appendChild(category);
    firstContainer.appendChild(secondContainer)

}
