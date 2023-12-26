def get_user(user_id: int):
    """Get user by ID."""

@users_router.get("/", response_model=dict)
def get_all_users():
    """Get all users."""

@users_router.post("/", response_model=dict)
def create_user():
    """Create a new user."""

@users_router.put("/{user_id}", response_model=dict)
def update_user(user_id: int):
    """Update user information."""

@users_router.delete("/{user_id}", response_model=dict)
def delete_user(user_id: int):
    """Delete user by ID."""
