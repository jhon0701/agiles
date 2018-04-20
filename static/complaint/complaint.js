$(document).ready(function(){
  // Time Picker
  jQuery('#timepicker').timepicker({
    defaultTIme : false
  });
  jQuery('#timepicker2').timepicker({
    showMeridian : false
  });
  jQuery('#timepicker3').timepicker({
    minuteStep : 15
  });
  
  // Date Picker
  jQuery('#datepicker').datepicker();
  jQuery('#datepicker-autoclose').datepicker({
    autoclose: true,
    todayHighlight: true
  });
  jQuery('#datepicker-inline').datepicker();
  jQuery('#datepicker-multiple-date').datepicker({
    format: "dd/mm/yyyy",
    clearBtn: true,
    multidate: true,
    multidateSeparator: ","
  });
  jQuery('#date-range').datepicker({
    toggleActive: true
  });

  // Validations
  $('input#datepicker').mask("99/99/9999");
  $('input#timepicker2').mask("99:99");
  $('input#id_license_plate').addClass("input-number");

});
