const { hostname, port } = window.location;
const ws = new WebSocket(`ws://${hostname}:${port}/ws`);
ws.onopen = () => {
  const connectionStatus = document.querySelector('[data-connection-status]');
  connectionStatus.classList.remove('badge-danger');
  connectionStatus.classList.add('badge-success');
  console.log('Connection ready!')
};
ws.onerror = (error) => console.error(error.message)
ws.onclose = () => {
  const connectionStatus = document.querySelector('[data-connection-status]');
  connectionStatus.classList.remove('badge-success');
  connectionStatus.classList.add('badge-danger');
  console.log('Connection closed!');
}
ws.onmessage = (e) => console.log(`Received ${e.data}`);

document.addEventListener('DOMContentLoaded', () => {
  const controls = document.querySelectorAll('[data-control]');
  for (let control of controls) {
    control.addEventListener('click', (e) => ws.send(control.getAttribute('data-control')));
  }
});
