$(document).ready(function () {
  
	$(".quanti-inc").click(function () {
		var $tr = $(this).closest("tr");
		var quantitySpan = $tr.find(".quanti");
		var currentQuantity = Number.parseInt(quantitySpan.text());
		var price = $tr.find(".price");
		var total = $tr.find(".total");
		currentQuantity++;
		total.text(currentQuantity * Number.parseFloat(price.text()));
		quantitySpan.text(currentQuantity);
    var sum = 0;
    $(".total").each(function () {
      var value = parseFloat($(this).text());
      if (!isNaN(value)) {
        sum += value;
      }
    })
    $("#total").text(sum);
	});

  var sum = 0;
    $(".total").each(function () {
      var value = parseFloat($(this).text());
      if (!isNaN(value)) {
        sum += value;
      }
    })
    $("#total").text(sum);
});
