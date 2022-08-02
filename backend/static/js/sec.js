$(document).ready(function(event){
    $(document).on('click', '#unlike', function(event){
      event.preventDefault();
      var pk = $(this).attr('value');
      $.ajax({
        type: "POST",
        url: '{% url "unlike_library" %}',
        data: {
          unlike_library_id:pk, 
          'csrfmiddlewaretoken': '{{csrf_token}}'
        },
        dataType: 'json',
        success: function(response){
          $('#unlike_section').html(response['form'])
          console.log($('#unlike_section').html(response['form']))
        },
  
        error: function (rs, e){
          console.log(rs.responseText);
  
        },
        
    });
  });
  });