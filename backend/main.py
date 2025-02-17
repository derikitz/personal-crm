from fastapi import FastAPI
from routes import user_routes
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(debug=True)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"], # Allow all methods
    allow_headers=["*"], # Allow all headers
)

# Include the user routes
app.include_router(user_routes.router, prefix="/users", tags=["users"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI + Supabase app!"}

# @app.get("/test-endpoint")
# async def test_endpoint():
#     try:
#         # Quering data from Supabase for testing.
#         response = supabase.table("users").select("*").execute()
        
#         # Check for errors
#         if not response.data:
#             return {"status": "error", "message": response.error.message}
        
#         # Return the data
#         return {"status": "success", "data": response.data}
#     except Exception as e:
#         return {"status": "error", "message": str(e)}