document.getElementById('submit').onclick = function (event) {
    event.preventDefault();
   let files = document.getElementById('json').files;

   if (files.length <= 0) {
    return false;
   }

   let fr = new FileReader();

   fr.onload = function(e) {
    let result = JSON.parse(e.target.result);
    let formatted = JSON.stringify(result, null, 2);

    try {
        const response = fetch("http://127.0.0.1:5000/api/convert", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: formatted
        })
        if (response.ok) {
            console.log('ok');
            const blob = response.blob();
            const downloadUrl = URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = downloadUrl;
            a. download = "archivo.zip";
            document.body.appendChild(a);
            a.click();
            a.remove();
            URL.revokeObjectURL(downloadUrl);
        }
    } catch (error) {
        console.log("Something went wrong...")
    }
   }
   fr.readAsText(files.item(0))
};