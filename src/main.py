import moviepy.editor as mp

from moviepy.editor import VideoFileClip


def resize_webm(input_path, output_path, max_width, max_height, max_duration, max_file_size):
    # Load the video clip
    clip = VideoFileClip(input_path)

    # Calculate the new dimensions while maintaining the aspect ratio
    width, height = clip.size
    aspect_ratio = width / height

    if width > height:
        new_width = min(max_width, width)
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = min(max_height, height)
        new_width = int(new_height * aspect_ratio)

    # Resize the video clip
    resized_clip = clip.resize((new_width, new_height))

    trimmed_clip = resized_clip.subclip(0, min(resized_clip.duration, max_duration))

    # Calculate the target bitrate to achieve the desired file size
    target_bitrate = int((max_file_size * 8) / trimmed_clip.duration)

    # Write the resized clip to the output file
    trimmed_clip.write_videofile(output_path, codec='libvpx', bitrate=f'{target_bitrate}k')

    # Close the clip to free up resources
    clip.close()
    resized_clip.close()
    trimmed_clip.close()


def convert_format(input_path, output_path):
    clip = mp.VideoFileClip(input_path)
    clip.write_videofile(output_path)


if __name__ == "__main__":
    input_file_path = "input/input.mp4"
    output_file_path = "output/output.webm"
    convert_format(input_file_path, output_file_path)
    resize_webm(output_file_path, output_file_path, 256, 256, 3, 256)
