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

document.getElementById("json_submit").addEventListener("click", async () => {
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
        {
            "type": "generic",
            "statement": ["QSBjb250aW51YWNpb24gbGEgZGVmaW5pY2lvbiBkZSBsYSBpbnRlZ3JhbCBwb3IgcGFydGVz", "XFtcaW50IHVkdj11di1caW50IHZkdVxd", "QmFzYWRvIGVuIGVzbywgcmVzdWVsdmEgbGFzIHNpZ3VpZW50ZXMgb3BlcmFjaW9uZXM="],
            "choices": [["SW50ZWdyYWwgZGVmaW5pZGFcXA=="],["XChcaW50IHhjb3MoeClkeFwp="],["XChcaW50IHhjb3MoeClkeFwp="],["XChcaW50IHhjb3MoeClkeFwp="]],
            "answer": ["XFsgeF5uICsgeV5uID0gel5uIFxd"]
        },
        {
            "type": "math",
            "statement": ["UmVzdWVsdmEgbGEgZWN1YWNpb24u"],
            "quantity": 1,
            "operation": "algebra_eq_int_one_step",
            "configuration": {
                "minimum_integer": 0,
                "maximum_integer": 10
            }
        },
        {
            "type": "math",
            "statement": ["UmVzdWVsdmEgbGEgZWN1YWNpb24u"],
            "quantity": 5,
            "operation": "arithmetic_int_add",
            "configuration": {
                "minimum_integer": 1,
                "maximum_integer": 10
            }
        },
        {
            "type": "math",
            "statement": ["UmVzdWVsdmEgbGEgZWN1YWNpb24u"],
            "quantity": 1,
            "operation": "arithmetic_int_sub",
            "configuration": {
                "minimum_integer": 0,
                "maximum_integer": 10
            }
        },
        {
            "type": "math",
            "statement": ["UmVzdWVsdmEgbGEgZWN1YWNpb24u"],
            "quantity": 10,
            "operation": "calculus_deriv_power",
            "configuration": {
                "minimum_exponent": 1,
                "maximum_exponent": 6,
                "minimum_coefficient": -10,
                "maximum_coefficient": 10
            }
        }
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