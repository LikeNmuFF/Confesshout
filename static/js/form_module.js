import { COURSES, YEAR_LEVEL } from './constant/constant.js';

function populateSelect(id, data){
    const select = document.getElementById(id);

    data.map((v) => {
        select.add(new Option(v.label, v.value));
    });
}


populateSelect("select_year", YEAR_LEVEL);
populateSelect("select_course", COURSES);