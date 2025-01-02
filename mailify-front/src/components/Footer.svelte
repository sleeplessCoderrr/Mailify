<script lang="ts">
    const currentYear: number = new Date().getFullYear();
  </script>
  
  <footer class="text-midnight py-6">
    <div class="container mx-auto px-4">
      <div class="flex flex-col gap-64 md:flex-row justify-between items-center md:items-start">
        <div class="mb-4 md:mb-0">
          <a href="/" class="text-2xl font-bold">Mailify</a>
          <p class="mt-2 text-sm">Simplifying job applications for Gen Z.</p>
        </div>
  
        <div class="grid grid-cols-2 gap-12 text-sm md:grid-cols-3 md:gap-32">
          <div>
            <h4 class="font-semibold mb-2">Company</h4>
            <ul>
              <li><a href="/about" class="hover:underline">About Us</a></li>
              <li><a href="/careers" class="hover:underline">Careers</a></li>
              <li><a href="/contact" class="hover:underline">Contact</a></li>
            </ul>
          </div>
          <div>
            <h4 class="font-semibold mb-2">Resources</h4>
            <ul>
              <li><a href="/blog" class="hover:underline">Blog</a></li>
              <li><a href="/help" class="hover:underline">Help Center</a></li>
              <li><a href="/privacy" class="hover:underline">Privacy Policy</a></li>
            </ul>
          </div>
          <div>
            <h4 class="font-semibold mb-2">Follow Us</h4>
            <ul>
              <li><a href="https://twitter.com" target="_blank" class="hover:underline">Twitter</a></li>
              <li><a href="https://linkedin.com" target="_blank" class="hover:underline">LinkedIn</a></li>
              <li><a href="https://instagram.com" target="_blank" class="hover:underline">Instagram</a></li>
            </ul>
          </div>
        </div>
      </div>
  
      <div class="mt-6 text-center text-sm border-t border-gray-700 pt-4">
        <p>&copy; {currentYear} Mailify. All rights reserved.</p>
      </div>
    </div>
  </footer>
  