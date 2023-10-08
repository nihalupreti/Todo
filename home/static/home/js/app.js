$(document).ready(function () {
  // Add a click event listener to checkboxes
  $(".todo__state").on("click", function () {
    // Get the task ID from the data attribute
    // const taskId = $(this).closest(".todo__wrapper").data("task-id");

    // Send an AJAX request to delete the task
    $.ajax({
      url: "/delete-task",
      type: "POST",
      // data: { task_id: taskId },
      headers: {
        "X-CSRFToken": csrfToken,
      },
      success: function (response) {
        if (response.status) {
          console.log(response);
          // window.location.href = response.redirect;
        }
      },
      error: function (error) {
        console.error("Error deleting task:", error);
      },
    });
  });
});
