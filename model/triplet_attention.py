import tensorflow as tf


class TripletAttention(tf.keras.layers.Layer):
    def __init__(self, kernel_size=7, **kwargs):
        super().__init__(**kwargs)
        self.kernel_size = kernel_size
        self.conv = tf.keras.layers.Conv2D(
            filters=1, kernel_size=kernel_size, padding='same', use_bias=False
        )

    def call(self, x):
        x_perm1 = tf.transpose(x, [0, 2, 3, 1])
        x_perm1 = tf.transpose(x_perm1, [0, 3, 1, 2])
        attn1 = tf.nn.sigmoid(self.conv(x))

        attn2_in = tf.transpose(x, [0, 2, 1, 3])
        attn2 = tf.nn.sigmoid(self.conv(attn2_in))
        attn2 = tf.transpose(attn2, [0, 2, 1, 3])

        attn3_in = tf.transpose(tf.transpose(x, [0, 3, 1, 2]), [0, 2, 3, 1])
        attn3 = tf.nn.sigmoid(self.conv(attn3_in))

        return (x * attn1 + x * attn2 + x * attn3) / 3.0

    def get_config(self):
        cfg = super().get_config()
        cfg.update({"kernel_size": self.kernel_size})
        return cfg
