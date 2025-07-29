document.addEventListener('DOMContentLoaded', function() {
    setDate();
});

function setDate() {
    const currentDate = new Date().toISOString().split('T')[0];
    document.getElementById('today').value = currentDate;
}