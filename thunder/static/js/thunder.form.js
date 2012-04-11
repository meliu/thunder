function isValidEmail (value) {
    var pattern = new RegExp("[\\w\\+-]+(\\.[\\w\\+-]+)?@((\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})\|([\\w\\+-]+\\.[a-zA-Z]{2,}))$");
    var pos = value.search(pattern);
    if (pos < 0) {
        return false;
    } else {
        return true;
    }
}
