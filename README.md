# Twitter-bot

The planned order that this will work
1. Fetch tweet, download it
2. Process the image attachment into an array which can be put through a Keras model
3. DO SOMETHING:
    * Neural style transfer: for example, make the image look horror-themed
    * Sentiment analysis: Is the image happy or sad? Tell the tweeter whether you like what they're showing you
    * Captioning: Write a witty caption
4. Store the output
5. Tweet the output
6. Remove inputs and outputs to save disk space

This is an attempt, more than anything, for me to get used to the Twitter API because from what I've used of it so far it's super fun and very easy to use. It would also be fun to play around with CNNs, or possibly some NLP if I need to generate captions.

To do: 
* Create a new Twitter account, get new access tokens etc and start working with that
* Set up the CNN (loading an image from file, process the image into a format we can input to a CNN, try to predict the label which is a short description of the image). Training/ideas: [link to blog post](https://towardsdatascience.com/image-captioning-with-keras-teaching-computers-to-describe-pictures-c88a46a311b8)
* Use pretrained VGG19 model (https://keras.io/applications/#vgg19) for Neural Style transfer or perhaps look into the `fast-style-transfer` page
