const headers = {
  "Content-Type": "application/json; charset=utf-8",
};

const server = 'http://192.168.99.102:5000'

const renderTask = (task) => {
  const rowTemplate = document.getElementById("task-row-template").innerHTML;
  const table = $("#task-table tbody");
  const htmlTask = Mustache.render(rowTemplate, task);
  table.append(htmlTask);
};

const updateTask = (taskId, progress, status, result) => {
  const taskRow = document.getElementById(taskId);
  const taskProgress = taskRow.querySelector("td[name=taskProgress]");
  const taskStatus = taskRow.querySelector("td[name=taskStatus]");
  const taskResult = taskRow.querySelector("td[name=taskResult]");

  taskProgress.innerHTML = `${progress ? ((progress.done / progress.total) * 100).toFixed(2) : 0} %`;
  taskStatus.innerHTML = status;
  taskResult.innerHTML = result ? result.result : null;
};

const listenTaskProgress = (taskId) => {
  const listenTask = setInterval(() => {
    fetch(`${server}/check-task/${taskId}`, {
      method: "GET",
      headers,
    })
      .then((res) => res.json())
      .then((res) => {
        const isSucess = res.status === "SUCCESS";
        updateTask(taskId, isSucess ? { done: 1, total: 1 } : res.progress, res.status, res.result || res.error);
        if (isSucess || res.status === "FAILURE") clearInterval(listenTask);
      });
  }, 2000);
};

const submitTask = (item) =>
  fetch(`${server}/item`, {
    method: "POST",
    body: JSON.stringify({ name: item }),
    headers,
  })
    .then((res) => res.json())
    .then((res) => {
      renderTask({ taskId: res.id, taskInput: item, taskStatus: "SENT", taskProgress: 0, taskResult: null });
      listenTaskProgress(res.id);
    });

const taskForm = $("#task-input-form");
taskForm.submit((event) => {
  submitTask($("#item-input").val());

  event.preventDefault();
  event.currentTarget.reset();
});
