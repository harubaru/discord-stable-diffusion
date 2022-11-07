# Shanghai - AI Powered Art in a Discord Bot!

<img src=https://cdn.discordapp.com/attachments/971549874514444358/1012400070559277086/1502073419.png?3867929 width=50% height=50%>

### Any questions or need help? Come hop on by to our Discord server!

[![Discord Server](https://discordapp.com/api/guilds/930499730843250783/widget.png?style=banner2)](https://discord.gg/Sx6Spmsgx7)

## Requirements
Unlike some other projects built around Stable Diffusion this Discord bot is setup only for NVIDIA GPUs and not optimized for low VRAM hardware.
Consult this table before attempting to run the bot:
| VRAM  | Comment |
| ------------- | ------------- |
| 10GB+  | Recommended - bot will run fine |
| 8GB-10GB  | Bot will most likely run |
| 6GB-8GB  | Bot might run - issues expected |
| <6GB  | Bot will probably not run, don't ask for support  |

## Setup
Make sure you have the [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) installed

Clone the repository and enter it
````
git clone https://github.com/harubaru/discord-stable-diffusion.git
cd discord-stable-diffusion
````

#### WINDOWS SETUP
Run `setup.bat`. If you run into any errors, try running the file as administrator

If you are on a Windows 10 system, run `win10patch.bat`

Modify the `run.bat` file, where
* `--model_path` is the path to the model (make sure to replace any backslashes with double backslashes),
* `--token=` is the token to the Discord bot
* `--hf_token=` is your huggingface token (can be found [here](https://huggingface.co/settings/tokens))

Run the `run.bat` file
#### LINUX SETUP
Run `./setup.sh`. If you run into any errors, try using `sudo ./setup.sh`

Modify the `run.sh` file, where
* `--model_path` is the path to the model,
* `--token=` is the token to the Discord bot
* `--hf_token=` is your huggingface token (can be found [here](https://huggingface.co/settings/tokens))

Run `./run.sh`

### Quickstart
#### Text to Image

To generate an image from text, use the ``/dream`` command and include your prompt as the query. There's tons of parameters to play with so go wild!

![image](https://user-images.githubusercontent.com/26317155/186722689-3cbca12a-531c-47f7-b87f-99918e9ed232.png)

![image](https://user-images.githubusercontent.com/26317155/186721768-3684f629-90c3-4ef2-82b8-1310200df437.png)


#### Image to Image

To generate an image from another image, use the ``/dream`` command and include the `init_image` and `strength` parameters. The image needs to be attached to the message.

![image](https://user-images.githubusercontent.com/26317155/186722463-ec3a6d24-36c1-48f8-b09a-57651706848c.png)

![image](https://user-images.githubusercontent.com/26317155/186722528-7e652a21-fd02-4071-9fc1-87a31dfb6e63.png)


#### (Experimental) Inpainting

To fill in a mask in an image, supply a prompt, the `init_image`, `mask_image` and `strength` parameters. The mask needs to consist of black pixels in a transparent image.

![image](https://user-images.githubusercontent.com/26317155/186722970-71a662dc-16a8-4bb4-8696-3bafb3e08e65.png)

