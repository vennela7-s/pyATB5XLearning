public_t = "PB"
def home():
    private_t = "PT"
    print(public_t)
    print(private_t)

def stranger():
    print(public_t)
    #print(private_t) cannot be used

print(public_t)
#local variables has more preference comparatively to public