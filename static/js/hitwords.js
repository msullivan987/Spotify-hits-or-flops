d3.csv("../datasets/hit_flop_words.csv").then(function(Data){

    var tbody = d3.select("tbody")
    
    // Data.forEach(function(data) {
    //     console.log(data)
        
    //   });
    
    // Step 2:  Use d3 to append one table row `tr` for each object
    Data.forEach(function(Data) {
        console.log(Data);
        var row = tbody.append("tr");
        
        Object.entries(Data).forEach(([key, value]) => {
            var cell = row.append("td");
            cell.text(value);
    });


    })
}); 