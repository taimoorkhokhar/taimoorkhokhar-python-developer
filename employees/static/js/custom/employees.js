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
        const form_data = new FormData();
        form_data.append("date", date);
        form_data.append("csrfmiddlewaretoken" , "{{csrf_token}}");
        $.ajax({
            url: "http://127.0.0.1:8000/api/employees/2021-06-14/?format=json",
            type:'GET',
            data: form_data,
            cache: false,
            processData: false,
            contentType: false,
            success: function (response) {
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
                    
                    $(".employeeTableByDate tbody tr:last").before(employeeTableRow);
                    
                    counter++   
                }
                bookMeetingBtns = $('.bookMeetingBtn');
                for (let clickEventCounter = 0; clickEventCounter < bookMeetingBtns.length; clickEventCounter++) {
                    bookMeetingBtns[clickEventCounter].addEventListener('click',  bookMeetingBtnsClickEvent.bind(this, clickEventCounter), false);
                }
                console.log(bookMeetingBtns)
            },
            error: function (data) {

            }
        });
    }

    function bookMeetingBtnsClickEvent(elementCounter, element){
        clickedButton = bookMeetingBtns[elementCounter]
        console.log("employee_id => ", clickedButton.getAttribute("data-employee-id"))
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