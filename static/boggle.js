class Boggle{
    
    constructor(){
        this.GUESSED_WORDS = [];
        this.timeOver = false;
        this.timer()
    }    
    
    async processGuess(guess) {
        const req = await axios.get('http://localhost:5000/check-word' , {params : {guess}});
    
        return req.data;
    }
    
    async submitHighScore(){
        const req = await axios.get('http://localhost:5000/submit-high-score');
        
        return req;
    }
    
    async endGame(){
        const res = await this.submitHighScore();
        
        $('#high-score').text(`highscore: ${res.data.highscore}`);
        
    }

    timer(){

        this.time = 0
        this.timerId = setInterval(() => {

            this.time++;
            $('#time').text(`time:${this.time}`);
            this.checkTime();

        }, 1000)

    }

    checkTime(){
        
        if(this.time === 60){
    
            clearInterval(this.timerId);
            $('#time').text(`times up!!`);
            this.timeOver = true;
            $('#word-fieldset').prop('disabled', true);
            this.endGame();

        }
    }
}

const boggleGame = new Boggle()

$('#check-word').on('submit', async function(evt){
    evt.preventDefault();

    if(!boggleGame.timeOver){

        const GUESS = $('#word-input').val();
        $('#word-input').val('')
        const res = await boggleGame.processGuess(GUESS);

        $('#response').text(res.result);
        
        if (boggleGame.GUESSED_WORDS.indexOf(res.guess.toUpperCase()) === -1){

            boggleGame.GUESSED_WORDS.push(res.guess.toUpperCase());
            
            $('#score').text(`score: ${res.score}`);

        }else{
            $('#response').text('Already Guessed This!');
        }
    }
})
