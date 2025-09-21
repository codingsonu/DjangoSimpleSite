import React, { useState, useEffect } from "react";
import axios from "axios";

const TaskForm = ({}) => {
  const [title, setTitle] = useState("");
  const [completed, setCompleted] = useState(false);
  const [tasks, setTasks] = useState([]);

  const fetchTasks = async () => {
    axios
      .get("http://127.0.0.1:8000/pages/tasks/") // thanks to proxy in package.json
      .then((response) => {
        setTasks(response.data.task); // 'task' key from your Django Response
      })
      .catch((error) => {
        console.error("Error fetching tasks:", error);
      });
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/pages/tasks/add/",
        {
          title,
          completed,
        }
      );
      console.log("Task added:", response.data);
      fetchTasks(); // Refresh the task list
      setTitle("");
      setCompleted(false);
    } catch (error) {
      console.error("Error adding task:", error);
    }
  };

  return (
    <>
      <div style={{ padding: "20px" }}>
        <h2>Task List</h2>
        <table
          border="1"
          cellPadding="8"
          style={{ width: "100%", textAlign: "left" }}
        >
          <thead>
            <tr>
              <th>ID</th>
              <th>Task Description</th>
              <th>Completed</th>
            </tr>
          </thead>
          <tbody>
            {tasks.length > 0 ? (
              tasks.map((task) => (
                <tr key={task.id}>
                  <td>{task.id}</td>
                  <td>{task.title}</td>
                  <td>{task.completed ? "✅ Yes" : "❌ No"}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="3">No tasks found</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Enter task title"
          required
        />
        <label>
          Completed:
          <input
            type="checkbox"
            checked={completed}
            onChange={() => setCompleted(!completed)}
          />
        </label>
        <button type="submit">Add Task</button>
      </form>
    </>
  );
};

export default TaskForm;
