/** Navbar Toggle */

const navbar = document.querySelector("[data-navbar]");
const navbarLinks = document.querySelectorAll("[data-nav-link]");
const menuToggleBtn = document.querySelector("[data-menu-toggle-btn]");

menuToggleBtn.addEventListener("click", function () {
  navbar.classList.toggle("active");
  this.classList.toggle("active");
});

for (let i = 0; i < navbarLinks.length; i++) {
  navbarLinks[i].addEventListener("click", function () {
    navbar.classList.toggle("active");
    menuToggleBtn.classList.toggle("active");
  });
}



/** Header toggle and Back to top */

const header = document.querySelector("[data-header]");
const backTopBtn = document.querySelector("[data-back-top-btn]");

window.addEventListener("scroll", function () {
  if (window.scrollY >= 100) {
    header.classList.add("active");
    backTopBtn.classList.add("active");
  } else {
    header.classList.remove("active");
    backTopBtn.classList.remove("active");
  }
});


// Form submission handler
document.getElementById('reservation-form').addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent the default form submission

  // Validate the form fields
  var name = document.getElementById('name').value;
  var email = document.getElementById('email').value;
  var numPersons = document.getElementById('num_persons').value;
  var date = document.getElementById('date').value;
  var time = document.getElementById('time').value;

  if (name.trim() === '' || email.trim() === '' || numPersons.trim() === '' || date.trim() === '' || time.trim() === '') {
    alert('Please fill in all fields.');
    return;
  }

  // Submit the form using AJAX
  var formData = new FormData(this);
  var xhr = new XMLHttpRequest();
  xhr.open('POST', this.action);
  xhr.setRequestHeader('X-CSRFToken', document.querySelector('input[name="csrfmiddlewaretoken"]').value);
  xhr.onload = function () {
    if (xhr.status === 200) {
      alert('Reservation submitted successfully!');
    } else {
      alert('An error occurred while submitting the reservation.');
    }
  };
  xhr.send(formData);
});

/** Move cycle on scroll */

const deliveryBoy = document.querySelector("[data-delivery-boy]");

let deliveryBoyMove = -80;
let lastScrollPos = 0;

window.addEventListener("scroll", function () {

  let deliveryBoyTopPos = deliveryBoy.getBoundingClientRect().top;

  if (deliveryBoyTopPos < 500 && deliveryBoyTopPos > -250) {
    let activeScrollPos = window.scrollY;

    if (lastScrollPos < activeScrollPos) {
      deliveryBoyMove += 1;
    } else {
      deliveryBoyMove -= 1;
    }

    lastScrollPos = activeScrollPos;
    deliveryBoy.style.transform = `translateX(${deliveryBoyMove}px)`;
  }

});

// Function to update table options based on selected date and time
function updateTableOptions() {
  var date = document.getElementById("date").value;
  var time = document.getElementById("time").value;
  var tableSelect = document.getElementById("table");

  // Make AJAX request to retrieve available tables based on date and time
  // Replace the AJAX URL with your endpoint for retrieving table availability
  var url = `/api/tables?date=${date}&time=${time}`;
  fetch(url)
    .then(response => response.json())
    .then(data => {
      // Clear existing options
      tableSelect.innerHTML = '<option value="" selected disabled>Select a table</option>';

      // Add new options based on retrieved data
      data.forEach(table => {
        var option = document.createElement("option");
        option.value = table.id;
        option.text = table.number + " (Capacity: " + table.capacity + ")";
        tableSelect.appendChild(option);
      });
    })
    .catch(error => {
      console.error('Error fetching table data:', error);
    });
}

// Add event listeners to date and time inputs to update table options
document.getElementById("date").addEventListener("change", updateTableOptions);
document.getElementById("time").addEventListener("change", updateTableOptions);

// Initial call to update table options based on default date and time values
updateTableOptions();