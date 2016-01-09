$(document).ready(function () {
    var ingredients = JSON.parse(localStorage.getItem("default.ingredients"));
    if (ingredients) {
        $("#listOfIngredients").html(ingredients);
        enableButtons("delete", "#listOfIngredients");
    }


    $("#dialog button").on("click", duplicateList);



    $("#btnSearch").on('click', searchItem);
    $("#searchText").on('keypress', searchItem);


    $("#btnCook").on('click', cookIngredients);

    $("#btnDeleteList").on('click', deleteList);
    $("#btnEmptyList").on('click', emptyIngredients);
    $("#btnDuplicate").on('click', openDialog);



    $("#listOfIngredients").droppable({
        drop: function (event, ui) {

            $("#listOfIngredients").append($(ui.draggable).clone());

            oddifyLines('#listOfIngredients li');

            enableButtons("delete", "#listOfIngredients");
            //store ingredients in local storage
            storeIngredients();
        }
    });

    dialog = $("#dialog").dialog({
        autoOpen: false,
        buttons: {
            "Add": duplicateList,
            Cancel: function () {
                dialog.dialog("close");
            }
        },
        close: function () {
            dialog.dialog("close");
        }
    });

});





function deleteList() {
    delete localStorage.getItem($.trim($("#currentList").text().toLowerCase()) + ".ingredients");
}

function duplicateList() {
    var newList = $("#newListName").val();

    $("#currentList").text(newList);
    $(".divider").before('<li><a href="#">' + newList + '</a></li>');


    localStorage.setItem($.trim($("#currentList").text().toLowerCase()) + ".ingredients", JSON.stringify($('#listOfIngredients').html()));

    $("#dialog").dialog("close");
}

function openDialog() {
    dialog.dialog("open");
}

function enableButtons(type, selector) {
    $("button." + type, selector).removeClass("hidden");

    if (type == "delete") {

        //Configure the button to remove the ingredient
        $(".delete").on("click", function (event) {
            $(event.target).parents("li").remove();
            storeIngredients();
        });
    }
}

function oddifyLines(selector) {
    $(selector).removeClass("odd").filter(":even").addClass("odd");
}

function storeIngredients() {
    localStorage.setItem($.trim($("#currentList").text().toLowerCase()) + ".ingredients", JSON.stringify($('#listOfIngredients').html()));
}

function emptyIngredients() {
    $("#listOfIngredients li").remove();
    storeIngredients();
}

function cookIngredients(event) {

    var data = {
        ingredients: $.map($("#listOfIngredients h5"), function (element, index) {
            return $(element).data("id")
        }).join(",")
    };

    $.ajax({
        url: "cook",
        crossDomain: true,
        dataType: "json",
        method: "POST",
        data: $.param(data),
        success: processCookedItems,
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(jqXHR, textStatus, errorThrown);
        }
    });
}

function processCookedItems(data) {
    console.log(data.package);
    $("#listOfBlueprints").html($.templates("#listOfItemsTmpl").render(data.package));

    enableButtons("info", "#listOfBlueprints");
    oddifyLines("#listOfBlueprints li");

    $("#numberOfInvestmentOptions").text(data.package.length);
}

function searchItem(event) {

    if (event.type == "keypress" && event.which != 13)
        return;

    var data = {};
    data.itemName = $.trim($("#searchText").val());

    $.ajax({
        url: "searchByItemName",
        crossDomain: false,
        dataType: "json",
        method: "POST",
        data: $.param(data),
        success: processSearchedItems,
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(jqXHR, textStatus, errorThrown);
        }
    });
}

function processSearchedItems(data) {
    console.log(data.package);
    $('#listOfItems').html($.templates("#listOfItemsTmpl").render(data.package));
    $('#listOfItems li').draggable({
        start: function () {
            $('#listOfIngredients').addClass('droppableArea')
        },
        stop: function () {
            $('#listOfIngredients').removeClass('droppableArea')
        },
        axis: "y",
        containment: ".panel",
        revert: true,
        zIndex: 100,
        helper: "clone",
        cursor: "crosshair",
        cursorAt: {
            bottom: 0
        }
    });

    oddifyLines('#listOfItems li');
}