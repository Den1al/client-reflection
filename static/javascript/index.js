function generateCookieArray() {
    let data = [];

    for (item of document.cookie.split(';')) {
        const firstEqual = item.indexOf('=');
        const name = item.substring(0, firstEqual);
        const value = item.substring(firstEqual + 1, item.length);

        data.push({ name, value });
    }

    return data;
}

$(document).ready(() => {
    let table = $('#cookies-table tbody');
    let data = generateCookieArray();

    console.log(data);

    $.each(data, (idx, elem) => {
        table.append(`<tr><td>${elem.name}</td><td>${elem.value}</td></tr>`);
    })
})