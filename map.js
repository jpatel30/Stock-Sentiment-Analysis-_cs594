
function map1() {

      //emit(this.symbol.symbol, this.symbol.id);
        
      var currentSymbol = this.symbol.symbol

       this.messages.forEach(function (m) {
        	currentBody = m.body;
        	//value= m.award_count;
          emit(currentSymbol, currentBody);
        });
}