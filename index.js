async function sendJsonAndGetZip(jsonText) {
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
    return await fetch('./data/question_types.json')
        .then((response) => {
            if (!response.ok) {
                throw new Error("Couldn't find JSON file.");
            }
            return response.json();
    })
}

async function getMathTypes() {
    return await fetch('./data/math_types.json')
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
    final_json.questions = [
        // Working on this lmao
    ];
            
    final_json.description = utf8_to_b64(final_json.description);
    final_json = JSON.stringify(final_json);

    try {
        const zipBlob = await sendJsonAndGetZip(final_json);
        console.log(zipBlob);
        const downloadBtn = document.createElement("button");
        downloadBtn.textContent = "Descargar";
        downloadBtn.id = "downloadBtn";
        document.body.appendChild(downloadBtn);

        downloadBtn.onclick = () => {
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

function createStatement(parent, placeholder) {
    const statement = document.createElement("input");
    statement.type = "text";
    statement.placeholder = placeholder;
    parent.appendChild(statement);
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
                mathQuestion(firstContainer, mathTypesJson);
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
                operation.appendChild(option);
            })

            const fourthContainer = document.createElement("div");

            operation.addEventListener("change", e => {
                const operationIndex = e.target.value;

                fourthContainer.innerHTML = '';

                const configuration = operations[operationIndex].configuration;
                const keys = Object.keys(configuration)
                for (let key of keys) {
                    const label = document.createElement("label");
                    label.textContent = key;
                    fourthContainer.appendChild(label);
                    createStatement(fourthContainer, configuration[key]);
                    fourthContainer.appendChild(document.createElement("br"));
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
