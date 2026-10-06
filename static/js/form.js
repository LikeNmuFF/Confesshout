function handleChange(e) {
    const status = e.target.checked;

    const label = e.target.parentElement;

    const name_field = document.getElementById("name_field");

    label.classList.toggle("checked");
    name_field.classList.toggle("disabled");

    if (status) {
        
        name_field.value = "";
        name_field.innerHTML = "";

        name_field.disabled = true
    } else {
        name_field.disabled = false
    }
}

const message_area = document.getElementById("message_area");
const textarea_char_count = document.getElementById("textarea_char_count");
message_area.addEventListener('input', (e) => {
    textarea_char_count.innerHTML = `${e.target.textLength}/500 Characters`;
})
