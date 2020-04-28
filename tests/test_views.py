import pyquery
import pytest


@pytest.mark.parametrize(
    "command,icon",
    (
        ("left", "arrow-left"),
        ("right", "arrow-right"),
        ("forward", "arrow-up"),
        ("reverse", "arrow-down"),
        ("stop", "hand-paper-o"),
    ),
)
def test_index_view_controls(client, command, icon):
    response = client.get("/")
    assert response.status_code == 200
    pq = pyquery.PyQuery(response.text)
    # A button with this command is found
    elements = pq(f'button[data-control="{command}"]')
    assert len(elements) == 1
    # It contains the appropriate icon
    assert elements.find("i").has_class(f"fa-{icon}")


@pytest.mark.parametrize("video_url", ("", "http://host/video.mjpg"))
def test_index_view_video(client, mocker, video_url):
    mocker.patch("raspycar.app.settings.VIDEO_URL", video_url)
    response = client.get("/")
    assert response.status_code == 200
    pq = pyquery.PyQuery(response.text)
    elements = pq('img[data-test="video"]')
    if video_url:
        assert len(elements) == 1
        assert elements.attr("src") == video_url
    else:
        assert len(elements) == 0


@pytest.mark.parametrize("command", ("left", "right", "forward", "reverse", "stop"))
def test_websocket(client, mocker, command):
    """Verify that commands are called on websocket data arrival"""
    mock = mocker.patch(f"raspycar.app.controls.{command}")
    with client.websocket_connect("/ws") as ws:
        ws.send_text(command)
    assert mock.called


def test_websocket_close_callback(client, mocker):
    """Verify callback is called when WS connection is closed"""
    mock = mocker.patch("raspycar.app.controls.stop")
    assert not mock.called
    with client.websocket_connect("/ws") as ws:
        ws.close()
    assert mock.called
