$(document).ready(function () {
  $(".todo__state").on("click", function () {
    const taskText = $(this)
      .closest(".todo__wrapper")
      .find(".todo__text")
      .text();

    // Send an AJAX request to delete the task
    $.ajax({
      url: "/delete-task",
      type: "POST",
      data: { user_todo: taskText },
      headers: {
        "X-CSRFToken": csrfToken,
      },
      success: function (response) {
        if (response.status) {
          console.log(response);
        }
      },
      error: function (error) {
        console.error("Error deleting task:", error);
      },
    });
  });

  // Add a new task when "Add Task" button is clicked
  $(".add-task-button").on("click", function () {
    const newTaskHtml = `
      <label class="todo">
        <div class="todo__wrapper">
          <input class="todo__state" type="checkbox" />
          <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 200 25" class="todo__icon">
            <use xlink:href="#todo__line" class="todo__line"></use>
            <use xlink:href="#todo__box" class="todo__box"></use>
            <use xlink:href="#todo__check" class="todo__check"></use>
            <use xlink:href="#todo__circle" class="todo__circle"></use>
          </svg>
          <input class="todo__text-input" type="text" placeholder="Enter your task..." />
        </div>
      </label>
    `;

    const $newTask = $(newTaskHtml);
    $(".todo-list").append($newTask);

    // Focus on the input field of the newly added task
    const $textInput = $newTask.find(".todo__text-input");
    $textInput.focus();

    // Handle saving a task when Enter is pressed or focus is lost
    $textInput.on("keydown blur", function (e) {
      if (e.type === "keydown" && e.key === "Enter") {
        e.preventDefault();

        const taskText = $(this).val();
        if (taskText.trim() === "") {
          // If the task text is empty, remove the task
          $(this).closest(".todo").remove();
        } else {
          // Replace the input field with the task text
          $(this).replaceWith(`<div class="todo__text">${taskText}</div>`);
          $.ajax({
            url: "/save-task",
            type: "POST",
            data: { added_todo: taskText },
            headers: {
              "X-CSRFToken": csrfToken,
            },
            success: function (response) {
              if (response.status) {
                console.log(response);
              }
            },
            error: function (error) {
              console.error("Error deleting task:", error);
            },
          });
        }
      } else if (e.type === "blur") {
        const taskText = $(this).val();
        if (taskText.trim() === "") {
          // If the input field loses focus and is empty, remove the task
          $(this).closest(".todo").remove();
        }
      }
    });
  });
});
