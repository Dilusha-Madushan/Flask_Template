function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((response) => {
        return response.json();
      
    }).then((data) => {
        if(data.status=='success'){
            window.location.href = "/";
        }else {
            const div = document.createElement("div");
            const btn = document.createElement("button");
            btn.setAttribute("class", "close");
            btn.setAttribute("data-dismiss" , "alert");
            const span = document.createTextNode("span");
            span.setAttribute("aria-hidden" , "true");
            span.innerHTML = "&times;";
            btn.appendChild(span);
            div.setAttribute("class" , "alert alert-danger alter-dismissable fade show");
            div.setAttribute("role" , "alert");
            div.appendChild(btn);
            document.getElementById("delete-fail") = div;
        }

    }).catch((error) => {
        alert(error)
    });
  }