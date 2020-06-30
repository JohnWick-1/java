    function average() {


        var eng = document.getElementById("eg").value;

        var math = document.getElementById("mt").value;

        var phy = document.getElementById("ph").value;

        var avg = (parseFloat(eng) + parseFloat(math) + parseFloat(phy))/3;


        document.getElementById("ag").value=avg.toFixed(2);

    }

