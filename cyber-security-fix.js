// Cyber Security Modal - Clean Implementation
document.addEventListener('DOMContentLoaded', function() {
    const cyberCard = document.getElementById('cyber-security-card');
    const cyberModal = document.getElementById('cyberSecurityModal');
    const closeCyberModal = document.getElementById('closeCyberModal');
    
    if (!cyberCard || !cyberModal || !closeCyberModal) return;
    
    // Clone the card to remove any existing event listeners
    const newCyberCard = cyberCard.cloneNode(true);
    cyberCard.parentNode.replaceChild(newCyberCard, cyberCard);
    
    // Function to show the modal
    function showModal() {
        // Hide all other modals
        document.querySelectorAll('.modal').forEach(m => m.style.display = 'none');
        // Show this modal
        cyberModal.style.display = 'block';
    }
    
    // Function to hide the modal
    function hideModal() {
        cyberModal.style.display = 'none';
    }
    
    // Add click handler to the card
    newCyberCard.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        showModal();
    }, true);
    
    // Add click handler to close button
    closeCyberModal.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        hideModal();
    }, true);
    
    // Close when clicking outside modal content
    cyberModal.addEventListener('click', function(e) {
        if (e.target === cyberModal) hideModal();
    });
    
    // Close with Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && cyberModal.style.display === 'block') {
            hideModal();
        }
    });
});
