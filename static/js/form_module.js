import { course, year_level } from './constant/constant.js';

function populateSelect(id, data){
    const select = document.getElementById(id);

    data.map((v) => {
        select.add(new Option(v.label, v.value));
    });
}


populateSelect("select_year", year_level);
populateSelect("select_course", course);