data = np.load("/content/drive/My Drive/Stocktopi Secret Sauce/dataset/dataset_processed.npy")
#14 by 8 by 8 input, where 12 of the 8 by 8s encode piece placements for either color and the other 2 encode legal moves
#^ no longer true, input shape is 513,
#every input is either 1 or 0
#evaluations in centipawns

trainx = data[:350000, 0:512]
trainy = data[:350000, -1:]
testx = data[350000:, 0:512]
testy = data[350000:, -1:]

model = tf.keras.models.Sequential([
    #tf.keras.layers.Flatten(input_shape = (8, 8, 8)),
    tf.keras.layers.Dense(256, activation = 'relu'),
    tf.keras.layers.Dense(32, activation = 'relu'),
    tf.keras.layers.Dense(1, activation = 'linear')
])

loss_fn = tf.keras.losses.MeanSquaredError()
model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = 0.003), loss = loss_fn)

model.fit(trainx, trainy, epochs = 5, batch_size = 1000)