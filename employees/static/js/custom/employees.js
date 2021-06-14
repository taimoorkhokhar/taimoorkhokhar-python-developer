$(document).ready(function () {
    // setTimeout(function(){
        const myInput = document.querySelector("#employeeDatePicker");
        // const config = {
        //     altInput: true,
        //     dateFormat: "YYYY-MM-DD",
        //     altFormat: "DD-MM-YYYY",
        //     allowInput: true,
        //     wrap: true,
        //     parseDate: (datestr, format) => {
        //       return moment(datestr, format, true).toDate();
        //     },
        //     formatDate: (date, format, locale) => {
        //       // locale can also be used
        //       return moment(date).format(format);
        //     }
        // }
        const fp = flatpickr(myInput, {});  // flatpickr
        fp.config.onChange.push(function(selectedDates, dateStr, instance) {
            console.log(dateStr)
            getEmployeesByDate(datestr)
        });
        // var e = document.getElementById("selectEmployeeDropdown");
        // var strUser = e.value;
        // console.log("strUser", strUser)

        // const chatBubbles = document.querySelectorAll('#mCSB_1 ul li a');
        // const sendMessage = document.querySelector('#send-message');
        // const chatProfileImage = $('.chat-profile-photo');
        // const chatProfileName = $('.chat-profile-name');
        // const chatOrganizationName = $('.chat-profile-name p');
        // const chatChannelName = $('.chat-profile-name p');
        // const typingAnimation = $('.chat-box .clearfix.typing-animation');
        

        // for (let clickEventCounter = 0; clickEventCounter < chatBubbles.length; clickEventCounter++) {
        //     chatBubbles[clickEventCounter].addEventListener('click',  chatBubblesClickEvent.bind(this, clickEventCounter), false);
        // }
        // sendMessage.addEventListener('click',  sendMessageClickEvent.bind(this, 0), false);


        // function sendMessageClickEvent(elementCounter, element){
            
        // }

        function getEmployeesByDate(date) {
            // console.log(collectiveName,channelName,assistantName, message)
            const form_data = new FormData();
            form_data.append("date", date);
            form_data.append("csrfmiddlewaretoken" , "{{csrf_token}}");
            $.ajax({
                url: "http://127.0.0.1/api/ask-question/?format=json",
                type:'POST',
                data: form_data,
                cache: false,
                processData: false,
                contentType: false,
                success: function (response) {
                    const collection = document.querySelectorAll('.clearfix.typing-animation.admin_chat');

                    for (const elem of collection) {
                        elem.remove();
                    }

                    let responseMessageHtml = `<li class="clearfix admin_chat">
                                                    <span class="chat-img">
                                                        <img src="/static/vendors/images/logo-icon.png" alt="">
                                                    </span>
                                                    <div class="chat-body clearfix">
                                                        <p>`+response[assistantName]+`</p>
                                                        <div class="chat_time">09:40PM</div>
                                                    </div>
                                                </li>`
                    $(".chat-box ul li:last").before(responseMessageHtml);
                    $("#mCSB_2").animate({ scrollTop: $("#mCSB_2")[0].scrollHeight}, {duration: 1000, complete: function(){
                        // const chatContainerHeight = $('#mCSB_2_container').height()
                        // $("#mCSB_2_container").css("top", -chatContainerHeight);
                    }});       
                },
                error: function (data) {

                }
            });
        }

    // }, 2000);
});