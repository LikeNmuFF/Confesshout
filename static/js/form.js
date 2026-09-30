function handleChange(e) {
    const status = e.target.checked;

    const label = e.target.parentElement;

    console.log(label.classList);

    if (status) {
        label.classList.toggle("checked");
    } else {
        label.classList.toggle('checked');
    }
}

const message_area = document.getElementById("message_area");
const textarea_char_count = document.getElementById("textarea_char_count");
message_area.addEventListener('input', (e) => {
    textarea_char_count.innerHTML = `${e.target.textLength}/50 Characters`;
})
