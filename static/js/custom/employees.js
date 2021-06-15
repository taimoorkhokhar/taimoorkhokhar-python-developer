$(document).ready(function () {
    const employeeDatePicker = document.querySelector("#employeeDatePicker");
    let employeesDic = {};
    let selectedDate = null;
    let firstEmployeeId = null;
    let secondEmployeeId = null;
    let meetingFromslot = null;
    let meetingToslot = null;
    let employeesByDateUrl = "http://127.0.0.1:8000/api/employees/";
    let employeesTimeSlotsUrl = "http://127.0.0.1:8000/api/meeting_slots/";
    let bookMeetingUrl = "http://127.0.0.1:8000/api/meeting_slots/";

    const fp = flatpickr(employeeDatePicker, {});  // flatpickr

    $('.alert.alert-success').close()

    fp.config.onChange.push(function(selectedDates, dateStr, instance) {
        selectedDate = dateStr
        getEmployeesByDate()
    });


    $("#bookMeetingform").submit(function(e) {
        e.preventDefault(); //prevent page from reloading on form submit
        bookMeetingApiCall()
    });


    function getEmployeesByDate() {
        $.ajax({
            url: employeesByDateUrl+selectedDate,
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
                const bookMeetingBtns = $('.bookMeetingBtn');
                for (let clickEventCounter = 0; clickEventCounter < bookMeetingBtns.length; clickEventCounter++) {
                    bookMeetingBtns[clickEventCounter].addEventListener('click',  bookMeetingBtnsClickEvent.bind(this), false);
                }
            },
            error: function (data) {

            }
        });
    }


    function getEmployeeTimeSlots(){
        $.ajax({
            url: employeesTimeSlotsUrl+selectedDate+"/"+firstEmployeeId+"/"+secondEmployeeId+"/",
            type:'GET',
            cache: false,
            processData: false,
            contentType: "application/json",
            dataType: "json",
            success: function (response) {
                $("#meetingSlotDropdown").empty();
                document.getElementById("meetingSlotDropdown").innerHTML += '<option value="" disabled selected>Select TimeSlots</option>'
                for (const dataDic of response.response) {
                    let employeeDropdownOption = `<option >`+dataDic.meeting_from_time+ " - " +dataDic.meeting_to_time+`</option>`
                    document.getElementById("meetingSlotDropdown").innerHTML += employeeDropdownOption
                }
                const meetingSlotDropdown = $('#meetingSlotDropdown');
                for (let clickEventCounter = 0; clickEventCounter < meetingSlotDropdown.length; clickEventCounter++) {
                    meetingSlotDropdown[clickEventCounter].addEventListener('change',  meetingSlotDropdownClickEvent.bind(this), false);
                }
            },
            error: function (data) {

            }
        });
    }


    function bookMeetingApiCall(){
        let data = {
            "meeting_from_time": meetingFromslot,
            "meeting_to_time": meetingToslot,
        }
        $.ajax({
            url: bookMeetingUrl+selectedDate+"/"+firstEmployeeId+"/"+secondEmployeeId+"/",
            type:'PUT',
            cache: false,
            processData: false,
            data:JSON.stringify( data),
            contentType: "application/json",
            dataType: "json",
            success: function (response) {
                console.log(response)
                $('#bookMeetingModal').modal('hide')
                $('.alert.alert-success').alert()
            },
            error: function (data) {

            }
        });
    }


    function meetingSlotDropdownClickEvent(element){
        const meetingTimeSlots = element.target.value.split(" - ")
        meetingFromslot = meetingTimeSlots[0]
        meetingToslot = meetingTimeSlots[1]
    }


    function bookMeetingBtnsClickEvent(element){
        clickedButton = element
        currentEmployeeId = clickedButton.target.getAttribute("data-employee-id")
        firstEmployeeId = currentEmployeeId
        $("#selectEmployeeDropdown").empty();
        $("#meetingSlotDropdown").empty();
        document.getElementById("selectEmployeeDropdown").innerHTML += '<option value="" disabled selected>Select Employee</option>'
        for (const dataDic of employeesDic) {
            if(currentEmployeeId != dataDic.employee_id ){
                let employeeDropdownOption = `<option value="`+dataDic.employee_id+`">`+dataDic.first_name+ " " + dataDic.last_name+`</option>`
                document.getElementById("selectEmployeeDropdown").innerHTML += employeeDropdownOption
            }
        }
        const employeeDropdown = $('#selectEmployeeDropdown');
        for (let clickEventCounter = 0; clickEventCounter < employeeDropdown.length; clickEventCounter++) {
            employeeDropdown[clickEventCounter].addEventListener('change',  employeeDropdownClickEvent.bind(this), false);
        }
    }

    function employeeDropdownClickEvent(element){
        secondEmployeeId = element.target.value
        getEmployeeTimeSlots()

    }
});