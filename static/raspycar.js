const { hostname, port } = window.location;
const ws = new WebSocket(`ws://${hostname}:${port}/ws`);
ws.onopen = () => console.log('Connection ready!');
ws.onerror = (error) => console.error(error.message)
ws.onclose = () => console.log('Connection closed!');
ws.onmessage = (e) => console.log(`Received ${e.data}`);

document.addEventListener('DOMContentLoaded', () => {
  const controls = document.querySelectorAll('[data-control]');
  for (let control of controls) {
    control.addEventListener('click', (e) => ws.send(control.getAttribute('data-control')));
  }
});
