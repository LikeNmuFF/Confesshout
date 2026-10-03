const request_panel = document.getElementById("request");
const empty_message = document.querySelector(".empty");
const table_container = request_panel.lastElementChild;
const table = table_container.lastElementChild;
const tbody = table.lastElementChild;

let isLoading = false;

function populateTable(data){
    const tr = document.createElement('tr');
    tbody.append(tr);

    const td_sender = document.createElement("td");
    td_sender.textContent = data.sender;

    tr.append(td_sender);

    const td_course = document.createElement('td');
    td_course.textContent = data.course;

    tr.append(td_course);

    const td_year_level = document.createElement("td");
    td_year_level.textContent = data.year_level;

    tr.append(td_year_level);

    const td_message_content = document.createElement("td");
    td_message_content.textContent = data.message_content;

    tr.append(td_message_content);

    const td_time_date = document.createElement('td');
    const date = document.createElement("p");
    date.classList.add("p-0", "m-0")
    date.textContent = data.submitted_date;
    td_time_date.append(date);
    const time = document.createElement("p");
    time.classList.add("p-0","m-0")
    time.textContent = data.submitted_time;
    td_time_date.append(time);

    tr.append(td_time_date);

    const td_actions = document.createElement('td');
    tr.append(td_actions);

    const btn_container = document.createElement("div");
    btn_container.classList.add("d-flex")
    td_actions.append(btn_container);

    const approve_btn = document.createElement("button");
    approve_btn.classList.add("btn","mx-1", "btn-success");
    approve_btn.textContent = "Approve";
    btn_container.append(approve_btn);

    const delete_btn = document.createElement("button");
    delete_btn.classList.add("btn", "btn-danger");
    delete_btn.textContent = "Delete";
    btn_container.append(delete_btn);
}

setInterval( async () => {
    if (isLoading) return;

    isLoading = true;

    try {
        const response = await fetch("/static/js/dummy/admin.json");

        if (response.ok){
            const data = await response.json();

            if(data && data.length > 0){
                empty_message.style.display = "none";
                table_container.style.display = "block";

                tbody.innerHTML = "";

                data.forEach(d => populateTable(d));
            }
        }
    } catch (error) {
        console.error(error);
    } finally {
        isLoading = false;
    }
}, 5000);