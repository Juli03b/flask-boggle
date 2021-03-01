$('#board-size-select').on('change', function(){
    let option = $("#board-size-select option:selected").val();
    
    if(option === 'custom-option'){
        $('#custom-input-div').append('<input type="number" name="custom-size" class="form-control mx-auto w-25 my-2" min="1" max="20" id="custom-size" placeholder="NxN" required>');
    }else{
        $("#custom-size").remove();
    }
});