from fastapi import FastAPI
import instaloader

app = FastAPI()

@app.get("/download_profile")
def download_profile():
    inst = instaloader.Instaloader()

    inst.login("wannacry_c", "Jancok123!")
    if not inst.context.is_logged_in:
        print("Login failed, using unauthenticated session") 
    else:
        print("Login success!")

    profile = instaloader.Profile.from_username(inst.context, 'gadissmanis2121')

    try:
        inst.download_profile(profile, "followers")
        return {"message": f"Profile downloaded successfully for {profile.username}"}
    except Exception as e:
        return {"message": f"Profile download failed. Error: {str(e)}. "}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)