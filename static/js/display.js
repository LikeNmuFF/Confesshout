function displayMessage(parent, data) {
    const container = document.createElement('div');
    container.classList.add('col-md-4');
    container.classList.add('col-lg-3');
    container.classList.add('col-xxl-2');
    container.classList.add('col-sm-12');
    container.classList.add('px-1');

    parent.append(container);

    const card = document.createElement('div');
    card.classList.add('card');
    card.classList.add('mb-2')

    container.append(card);

    const card_body = document.createElement('div');
    card_body.classList.add('card-body');

    card.append(card_body)

    const card_text = document.createElement('div');
    card_text.classList.add('card-text');

    const card_footer = document.createElement('div');
    card_footer.classList.add('card-footer');
    card_footer.classList.add('mt-2');
    card_footer.classList.add("px-0");
    card_footer.classList.add("py-2");
    card_footer.classList.add("d-flex");

    card_body.append(card_text);
    card_body.append(card_footer);

    card_text.innerHTML = data.content;

    const userText = document.createElement('div');
    if (data.username === "Anon") {
        userText.classList.add("bg-secondary");
        userText.classList.add("px-2");
        userText.classList.add("anon");
    } else {
        userText.classList.add("username");
    }
    userText.classList.add("py-1");
    userText.innerHTML = data.username;

    card_footer.append(userText);

    const course = document.createElement("div");
    course.classList.add('course');
    course.classList.add('mx-2');
    course.classList.add('py-1');
    course.classList.add('px-2');
    course.innerHTML = data.course;

    card_footer.append(course);

    const year = document.createElement('div');
    year.classList.add('year-level');
    year.classList.add('py-1');
    year.classList.add('px-2');
    year.innerHTML = data.year;

    card_footer.append(year);

    const time = document.createElement('div');
    time.classList.add("w-80");
    time.classList.add("time");
    time.classList.add("text-right");
    time.classList.add("py-1");
    time.classList.add("ml-auto");
    time.innerHTML = data.timestamp;

    card_footer.append(time);
}

setInterval(async () => {

    const api = "/static/js/dummy/display.json";

    try {
        const result = await fetch(api);

        if (result.ok) {
            const data = await result.json();

            if (data.length !== 0) {
                const empty_panel = document.getElementById("empty");

                if (empty_panel) {
                    empty_panel.style.display = "none";
                }

                const message_panel = document.getElementById("messages");

                if (data && data.length !== 0) {
                    message_panel.innerHTML = "";
                    data.map((d) => displayMessage(message_panel, d));

                    document.getElementById("displayed_message").innerHTML = `Displaying ${data.length} Messages`;
                }
            }
        }
    } catch (error) {
        console.error(error);
    }

}, 5000)