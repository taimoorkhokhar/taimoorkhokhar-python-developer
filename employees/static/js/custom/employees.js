$(document).ready(function () {
    let employeesDic = {};
    const employeeDatePicker = document.querySelector("#employeeDatePicker");
    let bookMeetingBtns = [];

    const fp = flatpickr(employeeDatePicker, {});  // flatpickr

    fp.config.onChange.push(function(selectedDates, dateStr, instance) {
        console.log(dateStr)
        getEmployeesByDate(dateStr)
    });


    function getEmployeesByDate(date) {
        $.ajax({
            url: "http://127.0.0.1:8000/api/employees/"+date,
            type:'GET',
            cache: false,
            processData: false,
            contentType: "application/json",
            dataType: "json",
            success: function (response) {
                document.getElementsByClassName("employeeTableBody")[0].innerHTML = "" // Delete Rows inside Table Body
                employeesDic = response.response;
                let counter = 1;
                for (const dataDic of response.response) {
                    console.log(dataDic)

                    let employeeTableRow = `<tr>
                                                <th scope="row">`+counter+`</th>
                                                <!-- First Name -->
                                                <td class="employeeFirstName">`+dataDic.first_name+`</td>
                                                <!-- Last Name --> 
                                                <td class="employeeLastName">`+dataDic.last_name+`</td>
                                                <td><button type="button" class="btn btn-primary btn-sm bookMeetingBtn" data-toggle="modal" data-target="#bookMeetingModal" data-employee-id=`+dataDic.employee_id+`>Book a Meeting</button></td>
                                                <td>
                                                    <input class="bookedTimeSlotTags" style="width:400px;" type="text" name="bookedTimeSlotTags"/>
                                                </td>
                                            </tr>`
                    document.getElementsByClassName("employeeTableBody")[0].innerHTML += employeeTableRow
                    counter++   
                }
                bookMeetingBtns = $('.bookMeetingBtn');
                for (let clickEventCounter = 0; clickEventCounter < bookMeetingBtns.length; clickEventCounter++) {
                    bookMeetingBtns[clickEventCounter].addEventListener('click',  bookMeetingBtnsClickEvent.bind(this, clickEventCounter), false);
                }
            },
            error: function (data) {

            }
        });
    }

    function bookMeetingBtnsClickEvent(elementCounter, element){
        clickedButton = bookMeetingBtns[elementCounter]
        currentEmployeeId = clickedButton.getAttribute("data-employee-id")
        $("#selectEmployeeDropdown").empty();
        for (const dataDic of employeesDic) {
            if(currentEmployeeId != dataDic.employee_id ){
                let employeeDropdownOption = `<option value="{{ data.employee_id }}">`+dataDic.first_name+ " " + dataDic.last_name+`</option>`
                document.getElementById("selectEmployeeDropdown").innerHTML += employeeDropdownOption
            }
        }
    }
});