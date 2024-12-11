import heapq
from collections import deque
import psutil

# Buffer Management Using Queues
class VideoBuffer:
    def __init__(self, max_size):
        self.buffer = deque(maxlen=max_size)

    def add_frame(self, frame):
        self.buffer.append(frame)  # Add new frame to buffer

    def get_frame(self):
        if self.buffer:
            return self.buffer.popleft()  # Retrieve the oldest frame
        return None

# Efficient File I/O Using Chunk-based Reading
def read_video_in_chunks(file_path, chunk_size):
    with open(file_path, 'rb') as video_file:
        while chunk := video_file.read(chunk_size):
            yield chunk

# Frame Indexing Using Dictionaries
class FrameIndexer:
    def __init__(self):
        self.index = {}

    def add_frame(self, timestamp, frame_data):
        self.index[timestamp] = frame_data

    def get_frame(self, timestamp):
        return self.index.get(timestamp, None)

# Playback Control Using Priority Queues
class PlaybackQueue:
    def __init__(self):
        self.queue = []

    def add_frame(self, priority, frame_data):
        heapq.heappush(self.queue, (priority, frame_data))

    def get_next_frame(self):
        if self.queue:
            return heapq.heappop(self.queue)[1]  # Return frame with the highest priority
        return None

# Lazy Loading for Efficient Memory Usage
class LazyVideoLoader:
    def __init__(self, file_path, chunk_size):
        self.file_path = file_path
        self.chunk_size = chunk_size
        self.reader = read_video_in_chunks(file_path, chunk_size)

    def load_next_chunk(self):
        try:
            return next(self.reader)
        except StopIteration:
            return None  # End of file

# Dynamic Buffer Size Adjustment
def adjust_buffer_size(current_buffer, max_memory_usage):
    available_memory = psutil.virtual_memory().available
    if available_memory < max_memory_usage:
        current_buffer.buffer = deque(maxlen=max(current_buffer.buffer.maxlen // 2, 10))  # Reduce size
    else:
        current_buffer.buffer = deque(maxlen=min(current_buffer.buffer.maxlen * 2, 1000))  # Increase size

# Integration and Playback
def video_stream(file_path, buffer_size, chunk_size, max_memory_usage):
    print("Initializing Video Streaming...")
    buffer = VideoBuffer(buffer_size)
    loader = LazyVideoLoader(file_path, chunk_size)

    while True:
        # Adjust buffer size dynamically
        adjust_buffer_size(buffer, max_memory_usage)

        # Fill buffer if not full
        while len(buffer.buffer) < buffer_size:
            chunk = loader.load_next_chunk()
            if not chunk:
                break  # End of file
            buffer.add_frame(chunk)

        # Retrieve and play frame
        frame = buffer.get_frame()
        if frame:
            print("Playing frame...")  # Replace with actual frame display logic
        else:
            print("Video Playback Complete.")
            break  # No more frames

# Driver Code
if __name__ == "__main__":
    # Path to the video file (update with the correct file path)
    video_file_path = "F:\DSA\Week 15/Video.mp4"
    
    # Configuration parameters
    buffer_size = 10         # Number of frames in buffer
    chunk_size = 1024 * 1024 # 1 MB chunks
    max_memory_usage = 500 * 1024 * 1024  # Max memory usage: 500 MB

    # Start the video streaming
    video_stream(video_file_path, buffer_size, chunk_size, max_memory_usage)
