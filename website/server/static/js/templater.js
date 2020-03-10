var createTemplate_Basic = function () {
  $.ajax({
    type: "POST",
    url: "templater/create-basic",
    data: JSON.stringify({
      template: $("#param-primary").val(),
      text: $("#input-text").val()
    }),
    contentType: "application/json",
    success: function (data) {
      $("#template-text").val(data.text);
    },
  });
};

var applyTemplate_Basic = function () {
  var template_tags = $("#param-template").val().trim().split(/[\s,.]+/g)
  $.ajax({
    type: "POST",
    url: "templater/apply-basic",
    data: JSON.stringify({
      templates: template_tags,
      filename: $("#param-filename").val(),
      text: $("#template-text").val()
    }),
    contentType: "application/json",
    xhrFields: {
      responseType: 'blob'
    },
    success: function (data, status, jqXHR) {
      var a = document.createElement("a");
      var url = window.URL.createObjectURL(data)
      a.href = url;
      a.download =
        jqXHR.getResponseHeader("content-disposition")
        .match(/filename="?(.+)"?/)[1];
      a.click();
      window.URL.revokeObjectURL(data)
    },
  });
};