$(document).ready(function () {
  // Basic client-side validation for register form
  $('#regForm').on('submit', function (e) {
    var valid = true;
    var name = $('#name').val().trim();
    var email = $('#email').val().trim();
    var phone = $('#phone').val().trim();
    var event_type = $('#event_type').val();

    // Reset
    $('#regForm .form-control, #regForm .form-select').removeClass('is-invalid');

    if (!name) {
      $('#name').addClass('is-invalid');
      $('#name').siblings('.invalid-feedback').show();
      valid = false;
    }

    // simple email regex
    var emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email || !emailRe.test(email)) {
      $('#email').addClass('is-invalid');
      $('#email').siblings('.invalid-feedback').show();
      valid = false;
    }

    if (phone) {
      var phoneRe = /^\d{10,12}$/;
      if (!phoneRe.test(phone)) {
        $('#phone').addClass('is-invalid');
        $('#phone').siblings('.invalid-feedback').show();
        valid = false;
      }
    }

    if (!event_type) {
      $('#event_type').addClass('is-invalid');
      $('#event_type').siblings('.invalid-feedback').show();
      valid = false;
    }

    if (!valid) {
      e.preventDefault();
      // show a small alert
      if ($('.client-alert').length === 0) {
        $('<div class="client-alert alert alert-warning mt-3">Please fix the highlighted fields and resubmit.</div>')
          .insertBefore('#regForm');
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  });

  // hide invalid-feedback on input
  $('#regForm input, #regForm select').on('input change', function () {
    if ($(this).hasClass('is-invalid')) {
      $(this).removeClass('is-invalid');
      $(this).siblings('.invalid-feedback').hide();
    }
  });
});
