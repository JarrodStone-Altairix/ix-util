var toggleCollapse = function (ele, toggle) {
  if (toggle) {
    $(ele).addClass("collapse")
  }
  else {
    $(ele).removeClass("collapse")
  }
}

var formatTable = function () {
  $.ajax({
    type: "POST",
    url: "fmt/table",
    data: JSON.stringify({ text: $("#input-text").val() }),
    contentType: "application/json",
    success: function (data) { $("#input-text").val(data.text); },
  });
};

var formatPivot = function () {
  $.ajax({
    type: "POST",
    url: "fmt/pivot",
    data: JSON.stringify({
      pivot: $("#pivot-regex").val(),
      text: $("#input-text").val()
    }),
    contentType: "application/json",
    success: function (data) { $("#input-text").val(data.text); },
  });
};

var format = function(formatType) {
  switch (formatType) {
    case "table":
      formatTable();
      break;
    case "pivot":
      formatPivot();
    default:
      break;
  }
}