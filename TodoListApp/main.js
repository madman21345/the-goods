window.addEventListener('load', () => {
    const form = document.querySelector("#new-task-form");
    const input = document.querySelector("#new-task-input");
    const list_el = document.querySelector("#tasks");

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const t = input.value;

        if(!t) {
            alert("please fill out a task");
            return;
        }

        const t_el = document.createElement("div"); 
        t_el.classList.add("task");

        const t_content_el = document.createElement("div"); //content or value
        t_content_el.classList.add("content");

        const t_in_el = document.createElement("input"); //input
        t_in_el.classList.add("text");
        t_in_el.type = "text";
        t_in_el.value = t;
        t_in_el.setAttribute("readonly", "readonly");

        const t_a_el = document.createElement("div");
        t_a_el.classList.add("actions");
        
        const t_e_el = document.createElement("button");
        t_e_el.classList.add("edit");
        t_e_el.innerText = "Edit";

        const t_d_el = document.createElement("button");
        t_d_el.classList.add("delete");
        t_d_el.innerText = "Delete";

        t_a_el.appendChild(t_e_el);
        t_a_el.appendChild(t_d_el);

        t_el.appendChild(t_content_el);
        t_content_el.appendChild(t_in_el);

        t_el.appendChild(t_a_el);
        list_el.appendChild(t_el);

        input.value = "";

        t_e_el.addEventListener('click', (e) => {
            if (t_e_el.innerText.toLowerCase() == "edit") {

                t_e_el.innerText = "Save";
                t_in_el.removeAttribute("readonly");
                t_in_el.focus();
            } else {
                t_e_el.innerText = "Edit";
                t_in_el.setAttribute("readonly", "readonly");
            }
        });

        t_d_el.addEventListener('click', (e) => {
            list_el.removeChild(t_el);
        });

    });
});