$(document).ready(function () {

    $("#menu-bar").click(() => {
        $("#menu-items").toggle();
    });

    $(".quanti-inc, .quanti-dec").click(function () {
        var $tr = $(this).closest("tr");
        var quantitySpan = $tr.find(".quanti");
        var currentQuantity = Number.parseInt(quantitySpan.text());
        var price = $tr.find(".price");
        var total = $tr.find(".total");
        if($(this).hasClass("quanti-inc")) currentQuantity++;
        else if($(this).hasClass("quanti-dec") && currentQuantity > 1) currentQuantity--;
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

    $('.add-to-cart').on('click', function () {
        var cart = $('.shopping-cart');
        console.log($(this).parent().parent().parent().parent().find("img").eq(0))
        var imgtodrag = $(this).parent().parent().parent().parent().find("img").eq(0);
        if (imgtodrag) {
            var imgclone = imgtodrag.clone()
                .offset({
                    top: imgtodrag.offset().top, left: imgtodrag.offset().left
                })
                .css({
                    'opacity': '0.8', 'position': 'absolute', 'height': '150px', 'width': '150px', 'z-index': '100'
                })
                .appendTo($('body'))
                .animate({
                    'top': cart.offset().top + 10, 'left': cart.offset().left + 10, 'width': 75, 'height': 75
                }, 1000, 'easeInOutExpo');

            setTimeout(function () {
                cart.effect("shake", {
                    times: 2
                }, 200);
            }, 1500);

            imgclone.animate({
                'width': 0, 'height': 0
            }, function () {
                $(this).detach()
            });
        }
    });
});
