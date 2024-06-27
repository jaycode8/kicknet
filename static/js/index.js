$("document").ready(function () { 
    $(".menubar").click(function () {
        // $(".menuItem").toggleClass("activeBar")
        // alert("hey")
        $(".menuItem").removeClass("-left-full");
    });
    $(".closemenubar").click(function () {
        // $(".menuItem").toggleClass("activeBar")
        // alert("hey")
        $(".menuItem").addClass("-left-full");
    });
});