const request_panel = document.getElementById("request");
const empty_message = document.querySelector(".empty");
const table_container = document.getElementById("requests-table");

let tbody;
let pending_messages;

if (table_container) {
    const table = table_container.lastElementChild;
    tbody = table.lastElementChild;
    pending_messages = table_container.firstElementChild;
}

let isLoading = false;

function populateTable(data) {
    const tr = document.createElement('tr');
    tbody.append(tr);

    const td_sender = document.createElement("td");
    if (data.username) {
        td_sender.textContent = data.username;
    } else {
        td_sender.textContent = "Anonymous";
    }
    tr.append(td_sender);

    const td_course = document.createElement('td');
    if (data.course) {
        td_course.textContent = data.course;
    } else {
        td_course.textContent = "N/A";
    }

    tr.append(td_course);

    const td_year_level = document.createElement("td");
    if (data.year_level) {
        td_year_level.textContent = data.year_level;
    } else {
        td_year_level.textContent = "N/A";
    }

    tr.append(td_year_level);

    const td_message_content = document.createElement("td");
    td_message_content.textContent = data.message;

    tr.append(td_message_content);

    const date_time = new Date(data.created_at.replace(" ", "T") + "Z").toLocaleString();

    const td_time_date = document.createElement('td');
    const date = document.createElement("p");
    date.classList.add("p-0", "m-0")
    date.textContent = date_time.split(" ")[0];
    td_time_date.append(date);
    const time = document.createElement("p");
    time.classList.add("p-0", "m-0")
    time.textContent = date_time.split(" ")[1];
    td_time_date.append(time);

    tr.append(td_time_date);

    const td_actions = document.createElement('td');
    tr.append(td_actions);

    const btn_container = document.createElement("div");
    btn_container.classList.add("d-flex")
    td_actions.append(btn_container);

    const approve_btn = document.createElement("button");
    approve_btn.classList.add("btn", "mx-1", "btn-success");
    approve_btn.textContent = "Approve";
    approve_btn.addEventListener("click", () => {
        fetch(`/api/admin/approve/${data.id}`, {
            method: "POST",
        });
    })
    btn_container.append(approve_btn);

    const delete_btn = document.createElement("button");
    delete_btn.classList.add("btn", "btn-danger");
    delete_btn.textContent = "Delete";

    delete_btn.addEventListener("click", () => {
        fetch(`/api/admin/reject/${data.id}`, {
            method: "POST"
        });
    });

    btn_container.append(delete_btn);
}

setInterval(async () => {
    if (isLoading) return;

    isLoading = true;

    try {
        const response = await fetch("/api/admin");

        if (response.ok) {
            const data = await response.json();

            if (data && data.length > 0) {
                if (empty_message) {
                    empty_message.style.display = "none";
                }

                if (!table_container) {
                    return window.location.reload();
                }

                table_container.style.display = "block";

                tbody.innerHTML = "";

                pending_messages.textContent = `Pending Messages (${data.length})`;
                data.forEach(d => populateTable(d));
            }else{
                if(!empty_message){
                    window.location.reload();
                }
            }
        }
    } catch (error) {
        console.error(error);
    } finally {
        isLoading = false;
    }
}, 5000);