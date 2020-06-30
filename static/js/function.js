    function average() {

        alert("hi")
        var eng = document.getElementById("eg").value;

        var math = document.getElementById("mt").value;

        var phy = document.getElementById("ph").value;

        int avg = (eng.value + math.value + phy.value);
        alert(eng)
        alert(math)
        alert(phy)
        alert(avg)

        document.getElementById("ag").value=avg;

        return avg;
    }